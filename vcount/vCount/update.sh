#!/bin/bash

SCRIPT=/tmp/reboot.sh

echo "#!/bin/bash" > $SCRIPT
echo "sleep 10" >> $SCRIPT
echo "/etc/init.d/server stop" >> $SCRIPT
echo "/etc/init.d/server start" >> $SCRIPT

chmod +x $SCRIPT

$SCRIPT&

exit 0
