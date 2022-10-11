export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

if  [[ -n ${14} ]] && [[ ${14} != "''" ]] && [[ ${14} != "NULL" ]]
then
  echo "${14}" > /tmp/ca_file.crt
  export TRACEABLE_ROOT_CA_FILE_NAME=/tmp/ca_file.crt
fi
if  [[ -n ${15} ]] && [[ ${15} != "''" ]] && [[ ${15} != "NULL" ]]
then
  echo "${15}" > /tmp/ca_cert.crt
  export TRACEABLE_CLI_CERT_FILE_NAME=/tmp/ca_cert.crt
fi
if  [[ -n ${16} ]] && [[ ${16} != "''" ]] && [[ ${16} != "NULL" ]]
then
    echo "${16}" > /tmp/ca_key.crt
  export TRACEABLE_CLI_KEY_FILE_NAME=/tmp/ca_key.crt
fi

traceableCliBinaryLocation=$1

scanInitCmd=$traceableCliBinaryLocation' ast scan initAndRun'
optionsArr=('--scan-name' '--traffic-env' '--token' '--plugins' '--include-url-regex' '--exclude-url-regex' '--target-url' '--traceable-server' '--idle-timeout' '--scan-timeout' ' --reference-env' '--max-retries')
stringArr=('--include-url-regex' '--exclude-url-regex' )

#Iterating the options available from options array and filling them with the arguments received in order
iterator=0
for option in "${@:2:12}"
do
  if [ -z "$option" ] || [ "$option" = "''" ] || [ "$option" = "NULL" ]
  then
    echo "${optionsArr[$iterator]}" is Null
  else
    presentInStringArr=0
    for subOption in "${stringArr[@]}"
    do
      if [ "$subOption" == "${optionsArr[$iterator]}" ]
      then
        presentInStringArr=1
      fi
    done
    if [ $presentInStringArr -eq 0 ]
    then
      scanInitCmd=$scanInitCmd"  "${optionsArr[$iterator]}" "${option}
    else
      scanInitCmd=$scanInitCmd"  "${optionsArr[$iterator]}" "\"${option}\"
    fi
  fi
  iterator=$(($iterator+1))
done

echo $scanInitCmd
$scanInitCmd