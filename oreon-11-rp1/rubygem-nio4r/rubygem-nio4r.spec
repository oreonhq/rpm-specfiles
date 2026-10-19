%global source0_hash 284aae4adc431498a8f2a8e6027da72bca5f2ea8134d770ffc6f8e45bf6b29f9
%global gem_name nio4r
%global libev_version 4.33
Name: rubygem-%{gem_name}
Version: 2.6.1
Release:        1%{?dist}
Summary:        New IO for Ruby
License: MIT AND (BSD-2-Clause OR GPL-2.0-or-later)
URL: https://github.com/socketry/nio4r
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  %{gem_name}-pr328-support-rubu35-openssl.patch
Provides: bundled(libev) = %{libev_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
EV_VERSION_MAJOR=$(grep EV_VERSION_MAJOR ext/libev/ev.h | cut -d ' ' -f3)
EV_VERSION_MINOR=$(grep EV_VERSION_MINOR ext/libev/ev.h | cut -d ' ' -f3)
[ "${EV_VERSION_MAJOR}.${EV_VERSION_MINOR}" = '%{libev_version}' ]
rspec -I$(dirs +1)%{gem_extdir_mri} spec
NIO4R_PURE=true rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-nio4r-doc -f %{oreon_filedir}/rubygem-nio4r-doc.list

%changelog

%autochangelog
