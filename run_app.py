from wsgiref import simple_server
import pecan

def setup_app(pecan_config=None, extra_hooks=None):

    if not pecan_config:
        pecan_config = get_pecan_config()

    pecan.configuration.set_config(dict(pecan_config), overwrite=True)

    app = pecan.make_app(
        pecan_config.app.root,
        static_root=pecan_config.app.static_root,
        template_path=pecan_config.app.template_path,
        force_canonical=getattr(pecan_config.app, 'force_canonical', True),
    )

    return app


conf = pecan.configuration.conf_from_file('cp_test_project/config.py')
root = setup_app(pecan_config=conf)
host = '0.0.0.0'
port = 8080
srv = simple_server.make_server(host, port, root)
if host == '0.0.0.0':
    print ('serving on 0.0.0.0:%s, view at http://127.0.0.1:%s' %
                 (port, port))
else:
    print ("serving on http://%s:%s" % (host, port))

try:
    srv.serve_forever()
except KeyboardInterrupt:
    # allow CTRL+C to shutdown without an error
    pass

