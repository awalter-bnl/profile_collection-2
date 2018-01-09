# Make ophyd listen to pyepics.
import nslsii

nslsii.configure_base(get_ipython().user_ns, 'cms')

from databroker.core import register_builtin_handlers
register_builtin_handlers(db.fs)


# At the end of every run, verify that files were saved and
# print a confirmation message.
# from bluesky.callbacks.broker import verify_files_saved
# RE.subscribe('stop', post_run(verify_files_saved))

# Optional: set any metadata that rarely changes.
# RE.md['beamline_id'] = 'YOUR_BEAMLINE_HERE'
# Uncomment the following lines to turn on verbose messages for debugging.
# import logging
# ophyd.logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)

from time import sleep
