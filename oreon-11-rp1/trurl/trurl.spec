%global source0_hash aac947d4fb421a58abc19a3771e87942cd4721b8f855c433478c94c11a8203ba

Name:           trurl
Version:        0.16.1
Release:        %autorelease
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

# Fix tests to use uppercase-hex
# https://github.com/curl/trurl/issues/394
Patch:          uppercase-hex.patch

# Fix discarded qualifiers
# https://github.com/curl/trurl/issues/430
Patch:          fix-discarded-qualifiers.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel

%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%check
make test

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md RELEASE-NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
