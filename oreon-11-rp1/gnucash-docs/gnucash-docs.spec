%global source0_hash 62f6f64b06ac1fe4c00efe5138a2fd1adc77c18223e88878d27ecc02df680588
Name: gnucash-docs
Summary:        Help files and documentation for the GnuCash personal finance manager
Version: 5.14
URL: https://gnucash.org/
Release:        2%{?dist}
License: GFDL-1.1-only
Source0:        https://downloads.sourceforge.net/gnucash/%{name}-%{version}.tar.gz
BuildArchitectures: noarch
Requires: yelp
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%pretrans -p <lua>

for _,d in pairs ({"gnucash-guide", "gnucash-help"}) do
  path = "%{_datadir}/gnome/help/" .. d
  if posix.stat(path, "type") == "link" then
    os.remove(path)
    posix.mkdir(path)
  end
end
return 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
