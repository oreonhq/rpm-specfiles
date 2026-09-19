%global source0_hash 13291beb06b602c87c3c04d544463692f900d27f026cf98e42c6e2838ab4a421

# No debugging info because the built .exe is bytecode. Re-enable
# if we get AOT working.
%global debug_package %{nil}

Name:           rescene
Version:        1.2
Release:        34%{?dist}
Summary:        Extracts RAR metadata and recreates RAR files
License:        MIT
# Upstream at http://rescene.info/ appears to have gone away. Mirror is
# maintained at:
URL:            http://rescene.wikidot.com/
Source0:        http://rescene.wdfiles.com/local--files/downloads/srr.%{version}.cs.zip

BuildRequires:  mono-core
Requires:       mono-core
ExclusiveArch:  %{mono_arches}

%description
ReScene is a mechanism for backing up and restoring the metadata from
RAR archives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cat >rescene.shell_script <<EOS
#!/bin/sh

mono "%{_libdir}/%{name}/srr.exe" "\$@"
EOS

# Fix EOL encodings
sed -i -e "s|\r||" license.txt

%build
mcs -unsafe -out:srr.exe *.cs

# Enabling AOT compilation causes rpmbuild to fail generating debuginfo.
# Disable it for now.
#mono --aot -O=all rescene.exe

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}

install -m 755 srr.exe $RPM_BUILD_ROOT%{_libdir}/%{name}/
# Enabling AOT compilation causes rpmbuild to fail generating debuginfo.
# Disable it for now.
#install -m 755 rescene.exe.so $RPM_BUILD_ROOT%%{_libdir}/%%{name}/
install -m 755 rescene.shell_script $RPM_BUILD_ROOT%{_bindir}/srr

%files
%doc license.txt
%{_libdir}/%{name}
%{_bindir}/srr

%changelog
%autochangelog
