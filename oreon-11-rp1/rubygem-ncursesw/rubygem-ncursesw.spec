%global source0_hash c897fc8165ca036fb2223e6f6ccdcedf5d2a1df5b1cd992e06af10b2d2858e62

%global gem_name ncursesw

Name:           rubygem-%{gem_name}
Version:        1.4.11
Release:        9%{?dist}
Summary:        Ruby wrapper for the ncurses library, with wide character support
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://github.com/sup-heliotrope/ncursesw-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
# https://github.com/sup-heliotrope/ncursesw-ruby/pull/40
# https://github.com/sup-heliotrope/ncursesw-ruby/commit/bd468ad296ed5bed2e51ad335858e0c92290e492
Patch0:         %{gem_name}-pr40-c23.patch
Requires:       ruby
BuildRequires:  ruby
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc
# rubygem Requires/Provides are automatically generated in F21+
%if ! (0%{?fedora} >= 21 || 0%{?rhel} >= 8)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

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
# examples are under a wide variety of licenses
# Automatically converted from old format: LGPLv2+ and MIT and MIT with advertising and LDPL - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-MIT-with-advertising AND LicenseRef-LDPL

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1 -b .c23

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications/ .%{gem_dir}/doc/ %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/{lib,examples} %{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/

%files
%license COPYING
%doc README.md Changes THANKS TODO
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/examples

%changelog
%autochangelog
