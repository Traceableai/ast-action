if [[ ${1}  = *"-rc."* ]]
then
  curl -OL https://downloads.traceable.ai/cli/rc/${1}/tars/traceable-cli-${1}-linux-x86_64.tar.gz
  tar -xvf ${GITHUB_WORKSPACE}/traceable-cli-${1}-linux-x86_64.tar.gz --directory ${GITHUB_WORKSPACE}
fi
if [[ ${1} = "latest" ]]
then
  curl https://s3.amazonaws.com/downloads.traceable.ai\?list-type\=2\&delimiter\=%2F\&prefix\=cli%2Frc%2Flatest%2Ftars%2F -o latest.xml
  tar_file="$( grep -z -o -p  'traceable-cli.*linux-x86_64.tar.gz' latest.xml | sed 's/traceable-cli//' | grep -o 'traceable-cli.*' )"
  curl -OL https://downloads.traceable.ai/cli/rc/latest/tars/${tar_file}
  tar -xvf ${GITHUB_WORKSPACE}/${tar_file} --directory ${GITHUB_WORKSPACE}
fi
