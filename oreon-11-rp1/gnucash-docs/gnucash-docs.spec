%global source0_hash none

Name: gnucash-docs
Summary: Help files and documentation for the GnuCash personal finance manager
Version: 5.14
URL: https://gnucash.org/
Release: 2%{?dist}
License: GFDL-1.1-only
Source: https://downloads.sourceforge.net/gnucash/%{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRequires: libxslt
BuildRequires: cmake make gcc gcc-c++
Requires: yelp

%description
GnuCash is a personal finance manager. gnucash-docs contains the
help files and documentation for GnuCash.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_datadir}/gnucash-docs/COPYING*

%files
%{_datadir}/help/*/gnucash*
%doc AUTHORS ChangeLog* NEWS README
%license COPYING*

%pretrans -p <lua>
for _,d in pairs ({"gnucash-guide", "gnucash-help"}) do
  path = "%{_datadir}/gnome/help/" .. d
  if posix.stat(path, "type") == "link" then
    os.remove(path)
    posix.mkdir(path)
  end
end
return 0

%changelog
%autochangelog
