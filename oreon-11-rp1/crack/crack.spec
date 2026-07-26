%global source0_hash 4b53627fd6f585d75a2fa74fed828596c4e91bef8972ec8972739bd7778dacf3

Summary:   Password cracker
Name:      crack
Version:   5.0a
Release:   54%{?dist}
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:   ClArtistic
Source:    ftp://ftp.cerias.purdue.edu/pub/tools/unix/pwdutils/crack/%{name}5.0.tar.gz
Patch0:    %{name}-chris.patch
Patch1:    %{name}-FHS.patch
Patch2:    %{name}-oldfun.patch
URL:       https://dropsafe.crypticide.com/alecm/software/crack/c50-faq.html
BuildRequires: words, gawk, gcc
BuildRequires: make
BuildRequires: libxcrypt-devel

%description
Crack is a password guessing program that is designed to quickly locate
insecurities in Unix (or other) password files by scanning the contents of a
password file, looking for users who have misguidedly chosen a weak login
password.

This package creates a group named "crack" and the Crack program puts all
its results in the /var/lib/crack/run directory, which belongs to that group.
Only users in the crack group can use this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n c50a
# Make sure we do not use libdes
rm -rf src/libdes
# select proper crypt routine and related checks
rm -f src/util/elcid.c
ln src/util/elcid.c,bsd src/util/elcid.c
mkdir run bin
# Try not to pollute bin namespace
sed -i -e 's/Reporter/CrackReporter/g' doc/gui.txt manual.html manual.txt
%patch -P0 -p1 -b .chris
sed -i 's|/usr/dict/|/usr/share/dict/|g' conf/dictgrps.conf
# Alter script to use FHS layout
%patch -P1 -p1 -b .FHS
%patch -P2 -p1 -b .oldfun

# Create a sysusers.d config file
cat >crack.sysusers.conf <<EOF
g crack -
EOF

%build
%global build_type_safety_c 0
C5FLAGS="-D_XOPEN_SOURCE -DUSE_STRING_H -DUSE_STDLIB_H -DUSE_SIGNAL_H -DUSE_SYS_TYPES_H -DUSE_UNISTD_H -DUSE_PWD_H"
make XDIR=../../bin XCC=gcc XCFLAGS="$RPM_OPT_FLAGS $C5FLAGS" XLIBS=-lcrypt utils
CRACK_HOME=`pwd` CRACK_BIN_HOME=`pwd` CRACK_STATE_DIR=`pwd` ./Crack -makedict

%install
rm -rf $RPM_BUILD_ROOT
rm -f bin/libc5.a bin/stdlib-cracker
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}
cp -a bin $RPM_BUILD_ROOT%{_libexecdir}/%{name} 
cp -a conf dict scripts $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a run $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}
install -p -m0755 Crack $RPM_BUILD_ROOT%{_bindir}/Crack
install -p -m0755 Reporter $RPM_BUILD_ROOT%{_bindir}/CrackReporter

install -m0644 -D crack.sysusers.conf %{buildroot}%{_sysusersdir}/crack.conf

%files
%doc LICENCE manual.* doc
%attr(00750, root, crack) %{_bindir}/Crack*
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%dir %{_sharedstatedir}/%{name}/
%attr(02770, root, crack) %dir %{_sharedstatedir}/%{name}/run/
%attr(02770, root, crack) %dir %{_sharedstatedir}/%{name}/run/dict/
%attr(00640, root, crack) %{_sharedstatedir}/%{name}/run/dict/*
%attr(00640, root, crack) %{_sharedstatedir}/%{name}/run/dict/.dictmade
%{_sysusersdir}/crack.conf

%changelog
%autochangelog
