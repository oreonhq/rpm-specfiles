%global source0_hash db4d78d9d36e387d7c714064bc9948c6105c017b32a977ebb27ae9b46ec10773

Summary: Calculates distance and azimuth between two Maidenhead locators
Name: wwl
Version: 1.3
Release: 13%{?dist}
License: wwl
URL: http://www.db.net/downloads/
Source: http://www.db.net/downloads/wwl+db-%{version}.tgz
BuildRequires: gcc
BuildRequires: make

%description
This program combines two handy ham radio Maindensquare programs into one.
When used as locator, it will take the Maindenhead square on the
command line and write it back out as lat / long.
When used as wwl, it will calculate distance and azimuth
between the two Maidenhead squares given.
If only four characters of the Maidenhead square is given, this
program will auto fill in the missing two chars with 'AA'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wwl+db-%{version}

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p "%{buildroot}%{_bindir}" "%{buildroot}%{_mandir}/man1"
%make_install PREFIX="%{buildroot}%{_prefix}" MAN1PREFIX="%{buildroot}%{_mandir}/man1/" LN="ln -r"
chmod 0644 %{buildroot}%{_mandir}/man1/wwl.1*

%files
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
