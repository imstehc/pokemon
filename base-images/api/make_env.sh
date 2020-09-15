#!/usr/bin/env bash
printenv | sed 's/^\(.*\)$/export \1/g' > env.sh
sed -i '/SAP_/d' env.sh
