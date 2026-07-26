%global source0_hash 3d3e39d569e44677c4b179129bde614c65798e2b3e6253160239d1fd6eae4d79

%global src_name buildsystem

Name:           netsurf-buildsystem
Version:        1.10
Release:        %autorelease
Summary:        Makefiles shared by NetSurf projects
License:        MIT
URL:            http://www.netsurf-browser.org/
Source0:        http://download.netsurf-browser.org/libs/releases/%{src_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators

%description
%{name} contains makefiles shared by NetSurf projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{src_name}-%{version} -p1

sed -i -e 1s@/bin/@/usr/bin/@ testtools/testrunner.pl
chmod +x testtools/testrunner.pl

%install
%make_install PREFIX=%{_prefix}

%files
%doc README
%license COPYING
%{_datadir}/%{name}/

%changelog
%autochangelog
