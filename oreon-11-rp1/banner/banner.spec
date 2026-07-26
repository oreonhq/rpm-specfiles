%global source0_hash a488df83d9de1fcc8296cd332668c3d2a05e6685b19b5e779207d94d99e9f88e

Name:           banner
Summary:        Prints a short string to the console in very large letters

Version:        1.3.6
Release:        %autorelease

License:        GPL-2.0-only
BuildRequires:  gcc
BuildRequires:  make
URL:            https://github.com/pronovic/banner
Source0:        https://github.com/pronovic/banner/releases/download/BANNER_V%{version}/banner-%{version}.tar.gz

%description
Classic-style banner program similar to the one found in Solaris or AIX.
The banner program prints a short string to the console in very large
letters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/banner
%{_mandir}/man1/banner*

%changelog
%autochangelog
