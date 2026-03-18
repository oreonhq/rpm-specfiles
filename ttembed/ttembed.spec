Name:       ttembed
Version:    1.1
Release:    25%{?dist}
Summary:    Remove embedding limitations from TrueType fonts
License:    Unlicense
URL:        https://github.com/hisdeedsaredust/ttembed
Source0:    https://github.com/hisdeedsaredust/ttembed/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Remove embedding limitations from TrueType fonts, by setting the fsType field
in the OS/2 table to zero. That's it; this program is a one-trick pony.

%prep
%setup -q

%build
export CFLAGS="$CFLAGS %{optflags}"
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1/
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/*
%doc LICENSE README.md

%check
# smoke test - fail on not font file
echo 'not a font' > test
if [[ "$(./ttembed test 2>&1)" != "test: Not TTF/OTF" ]] ; then
    echo "TEST FAIL: not a font input test" 1>&2
    exit 1
fi
rm test

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-25
- Prepare for Oreon 11 (RP1)
