%global source0_hash fe4b731b14456da210966bfa5e6c9cc6e99ace1905537eb5df2d4dcf940fedd1

Name:           wipe
Version:        0.21
Release:        34%{?dist}
Summary:        Secure file erasing tool

License:        GPL-1.0-or-later
URL:            http://abaababa.ouvaton.org/wipe/
Source0:        http://abaababa.ouvaton.org/wipe/wipe-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Wipe is a little command for securely erasing files from magnetic media. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
chmod +x trtur
export CFLAGS=$RPM_OPT_FLAGS
make %{?_smp_mflags} linux
iconv -f ISO8859-9 -t UTF8 <README > README.utf8
mv README.utf8 README
iconv -f ISO8859-9 -t UTF8 <wipe.tr.1 > wipe.tr.1.utf8
mv wipe.tr.1.utf8 wipe.tr.1
chmod a-x examples/wipefd0 examples/wswap.pl

%install
rm -rf $RPM_BUILD_ROOT
# There is no make install.
# So, we do the install ourselves due to so few files to install.
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1,%{_mandir}/tr/man1}
install -p wipe $RPM_BUILD_ROOT/%{_bindir}
install -p -m644 wipe.1 $RPM_BUILD_ROOT/%{_mandir}/man1
mv wipe.tr.1 wipe.1 && \
  install -p -m644 wipe.1 $RPM_BUILD_ROOT/%{_mandir}/tr/man1/

%files
%doc BUGS CHANGES GPL README examples/wipefd0 examples/wswap.pl
%{_bindir}/wipe
%{_mandir}/man1/wipe.1.gz
%{_mandir}/tr/man1/wipe.1.gz

%changelog
%autochangelog
