if [[ ${1}  = *"-rc."* ]]
then
  curl -OL https://downloads.traceable.ai/cli/rc/${1}/tars/traceable-cli-${1}-linux-x86_64.tar.gz
  tar -xvf ${GITHUB_WORKSPACE}/traceable-cli-${1}-linux-x86_64.tar.gz --directory ${GITHUB_WORKSPACE}
fi
if [[ ${1} = "latest" ]]
then
  tar_file="$( curl -s https://s3.amazonaws.com/downloads.traceable.ai\?list-type=2\&delimiter\=%2F\&prefix=cli%2Frc%2Flatest%2Ftars%2F |  grep -z -o --text  'traceable-cli.*linux-x86_64.tar.gz' | sed 's/traceable-cli//' | grep -o -a 'traceable-cli.*'  )"
  echo ${tar_file}
  curl -OL https://downloads.traceable.ai/cli/rc/latest/tars/${tar_file}
  tar -xvf ${tar_file} --directory ${GITHUB_WORKSPACE}
fi