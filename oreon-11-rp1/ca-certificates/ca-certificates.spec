%global source0_hash ba6014fa6c7eaefb22dd977fb8a8d297237ea867f3c18c6c4dd53fad5180a1f7
%define pkidir %{_sysconfdir}/pki
%define catrustdir %{_sysconfdir}/pki/ca-trust
%define p11_format_bundle ca-bundle.trust.p11-kit
%define legacy_default_bundle ca-bundle.legacy.default.crt
%define legacy_disable_bundle ca-bundle.legacy.disable.crt
%define java_bundle java/cacerts
Summary:        The Mozilla CA root certificate bundle
Name: ca-certificates
Version: 2025.2.80_v9.0.304
Release:        6%{?dist}
License: MIT AND GPL-2.0-or-later
URL: https://fedoraproject.org/wiki/CA-Certificates
Source0:        certdata.txt
Source1: nssckbi.h
Source2: update-ca-trust
Source3: trust-fixes
Source4: certdata2pem.py
Source5: ca-legacy.conf
Source6: ca-legacy
Source9: ca-legacy.8.txt
Source10: update-ca-trust.8.txt
Source11: README.usr
Source12: README.etc
Source13: README.extr
Source14: README.java
Source16: README.pem
Source17: README.edk2
Source18: README.src
Source19: README.etcssl
BuildArch: noarch
Requires(post): bash
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): coreutils
Requires: bash
Requires: grep
Requires: sed
Requires(post): p11-kit >= 0.24
Requires(post): p11-kit-trust >= 0.24
Requires: p11-kit >= 0.24
Requires: p11-kit-trust >= 0.24
Requires: libffi
Requires(post): libffi
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  openssl
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  xmlto
# /oreon:deps
%description
This package contains the set of CA certificates chosen by the
Mozilla Foundation for use with the Internet PKI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
rm -rf %{name}
mkdir %{name}
mkdir %{name}/certs
mkdir %{name}/certs/legacy-default
mkdir %{name}/certs/legacy-disable
mkdir %{name}/java

%build

pushd %{name}/certs
 pwd
 cp %{SOURCE0} .
 python3 %{SOURCE4} >c2p.log 2>c2p.err
popd
pushd %{name}
 (
   cat <<EOF
EOF
   cat %{SOURCE1}  |grep -w NSS_BUILTINS_LIBRARY_VERSION | awk '{print "# " $2 " " $3}';
   echo '#';
 ) > %{p11_format_bundle}
 touch %{legacy_default_bundle}
 NUM_LEGACY_DEFAULT=`find certs/legacy-default -type f | wc -l`
 if [ $NUM_LEGACY_DEFAULT -ne 0 ]; then
     for f in certs/legacy-default/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy default flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_default_bundle}
       fi
     done
 fi
 touch %{legacy_disable_bundle}
 NUM_LEGACY_DISABLE=`find certs/legacy-disable -type f | wc -l`
 if [ $NUM_LEGACY_DISABLE -ne 0 ]; then
     for f in certs/legacy-disable/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy disable flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_disable_bundle}
       fi
     done
 fi
 P11FILES=`find certs -name \*.tmp-p11-kit | wc -l`
 if [ $P11FILES -ne 0 ]; then
   for p in certs/*.tmp-p11-kit; do 
     cat "$p" >> %{p11_format_bundle}
   done
 fi
 cat %{SOURCE3} >> %{p11_format_bundle}
popd
cp %{SOURCE10} %{name}/update-ca-trust.8.txt
asciidoc -v -d manpage -b docbook %{name}/update-ca-trust.8.txt
xmlto -v -o %{name} man %{name}/update-ca-trust.8.xml
cp %{SOURCE9} %{name}/ca-legacy.8.txt
asciidoc -v -d manpage -b docbook %{name}/ca-legacy.8.txt
xmlto -v -o %{name} man %{name}/ca-legacy.8.xml
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 $RPM_BUILD_ROOT%{pkidir}/tls/certs
mkdir -p -m 755 $RPM_BUILD_ROOT%{pkidir}/java
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/ssl
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/blocklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem
mkdir -p -m 555 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/directory-hash
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/java
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/blocklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 %{name}/update-ca-trust.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 %{name}/ca-legacy.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/README
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{catrustdir}/README
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{catrustdir}/extracted/README
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{catrustdir}/extracted/java/README
install -p -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/README
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/README
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{catrustdir}/source/README
install -p -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/README
install -p -m 644 %{name}/%{p11_format_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{p11_format_bundle}
install -p -m 644 %{name}/%{legacy_default_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
install -p -m 644 %{name}/%{legacy_disable_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{catrustdir}/ca-legacy.conf
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{p11_format_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update-ca-trust
install -p -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/ca-legacy
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/tls-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/tls-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/email-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/email-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/objsign-ca-bundle.pem
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/objsign-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/%{java_bundle}
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/%{java_bundle}
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/cacerts.bin
chmod 444 $RPM_BUILD_ROOT%{catrustdir}/extracted/edk2/cacerts.bin
if test "$(id -u)" -eq 0; then
   trust_module_dir=/etc/pkcs11/modules
else
   trust_module_dir=$HOME/.config/pkcs11/modules
fi
mkdir -p "$trust_module_dir"
if [ -n "$(ls -A "$trust_module_dir")" ]; then
        echo "Directory $trust_module_dir is not empty. Aborting build!"
        exit 1
fi
trust_module_config=$trust_module_dir/%{name}-p11-kit-trust.module
cat >"$trust_module_config" <<EOF
module: p11-kit-trust.so
trust-policy: yes
x-init-reserved: paths='$RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source'
EOF
trust extract --format=pem-directory-hash --filter=ca-anchors --overwrite \
              --purpose server-auth \
              $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/directory-hash
rm -f "$trust_module_config"
find $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/directory-hash -type l \
     -regextype posix-extended -regex '.*/[0-9a-f]{8}\.[0-9]+' \
     -exec cp -P {} $RPM_BUILD_ROOT%{pkidir}/tls/certs/ \;
find $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/directory-hash -type f,l > .files.txt
find $RPM_BUILD_ROOT%{pkidir}/tls/certs -type l -regextype posix-extended \
     -regex '.*/[0-9a-f]{8}\.[0-9]+' >> .files.txt
sed -i "s|^$RPM_BUILD_ROOT|%ghost /|" .files.txt
ln -s %{pkidir}/tls/certs \
    $RPM_BUILD_ROOT%{_sysconfdir}/ssl/certs
ln -s /etc/pki/tls/openssl.cnf \
    $RPM_BUILD_ROOT%{_sysconfdir}/ssl/openssl.cnf
ln -s /etc/pki/tls/ct_log_list.cnf \
    $RPM_BUILD_ROOT%{_sysconfdir}/ssl/ct_log_list.cnf
ln -s %{catrustdir}/extracted/%{java_bundle} \
    $RPM_BUILD_ROOT%{pkidir}/%{java_bundle}
%clean
/usr/bin/chmod u+w $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/directory-hash
rm -rf $RPM_BUILD_ROOT
%oreon_autofiles main

%pre

if [ $1 -gt 1 ] ; then
  rm -f %{pkidir}/tls/cert.pem
  rm -f %{pkidir}/tls/certs/ca-bundle.crt
  rm -f %{pkidir}/tls/certs/ca-bundle.trust.crt
  rm -f %{pkidir}/tls/certs/ca-certificates.crt
  rm -f %{_sysconfdir}/ssl/cert.pem
  if ! test -e %{pkidir}/%{java_bundle}.rpmsave; then
    if test -e %{pkidir}/%{java_bundle}; then
        if ! test -L %{pkidir}/%{java_bundle}; then
        mv -f %{pkidir}/%{java_bundle} %{pkidir}/%{java_bundle}.rpmsave
      fi
    fi
  fi
fi
%post

if [ -x %{_bindir}/ln ]; then
%{_bindir}/ca-legacy install
%{_bindir}/update-ca-trust
fi
%posttrans

%{_bindir}/ca-legacy install
%{_bindir}/update-ca-trust
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
