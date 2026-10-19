%global source1_hash 9b8e17ceed1a7a9ef0a4c7d7cf35c467d9c3609e95ca0463dcda7fd7ad175411
%global source0_hash 2a467db7620243af86aaf146aaa5b2cb7228a5646a013d8558cd240f7cf6e3b4
%global gem_name ethon
Name: rubygem-%{gem_name}
Version: 0.17.0
Release:        1%{?dist}
Summary:        Libcurl wrapper
License: MIT
URL: https://github.com/typhoeus/ethon
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/typhoeus/ethon/archive/refs/tags/v0.17.0.tar.gz
Patch0: rubygem-ethon-0.17.0-fix-on-headers-regression.patch
Patch1: rubygem-ethon-0.17.0-fix-on-headers-regression-test.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(mime-types)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rackup)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(sinatra)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Very lightweight libcurl wrapper.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{builddir}/spec spec
sed -i -e "/require 'bundler'/ s/^/#/" \
       -e "/Bundler.setup/ s/^/#/" \
       spec/spec_helper.rb
rspec -r rackup spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ethon-doc -f %{oreon_filedir}/rubygem-ethon-doc.list

%changelog

%autochangelog
