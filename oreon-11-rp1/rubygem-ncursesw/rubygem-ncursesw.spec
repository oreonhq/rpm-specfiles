%global source0_hash c897fc8165ca036fb2223e6f6ccdcedf5d2a1df5b1cd992e06af10b2d2858e62
%global gem_name ncursesw
Name:           rubygem-%{gem_name}
Version:        1.4.11
Release:        1%{?dist}
Summary:        Ruby wrapper for the ncurses library, with wide character support
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://github.com/sup-heliotrope/ncursesw-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         %{gem_name}-pr40-c23.patch
Requires:       ruby
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This wrapper provides access to the functions, macros, global variables and 
constants of the ncurses library. These are mapped to a Ruby module named 
"Ncurses". Functions and external variables are implemented as singleton 
functions of the module Ncurses.

The ncursesw gem is a fork with improved wide character support.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-MIT-with-advertising AND LicenseRef-LDPL
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1 -b .c23

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications/ .%{gem_dir}/doc/ %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/{lib,examples} %{buildroot}%{gem_instdir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-ncursesw-doc -f %{oreon_filedir}/rubygem-ncursesw-doc.list

%changelog

%autochangelog
