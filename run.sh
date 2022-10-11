export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

if [ -f "/tmp/ca_file.crt" ]
then
  export TRACEABLE_ROOT_CA_FILE_NAME=/tmp/ca_file.crt
fi
if  [ -f "/tmp/ca_cert.crt" ]
then
  export TRACEABLE_CLI_CERT_FILE_NAME=/tmp/ca_cert.crt
fi
if  [ -f "/tmp/ca_key.crt" ]
then
  export TRACEABLE_CLI_KEY_FILE_NAME=/tmp/ca_key.crt
fi

traceableCliBinaryLocation=$1

scanRunCmd=$traceableCliBinaryLocation' ast scan run '
optionsArr=('--token' '--idle-timeout' '--max-retries' )

#Iterating the options available from options array and filling them with the arguments received in order
iterator=0
for option in "${@:2:3}"
do
  if [ -z "$option" ] || [ "$option" = "''" ] || [ "$option" = "NULL" ]
  then
    echo "${optionsArr[$iterator]}" is Null
  else
    scanRunCmd=$scanRunCmd" "${optionsArr[$iterator]}" "${option}
  fi
  iterator=$(($iterator+1))
done

echo $scanRunCmd
$scanRunCmd