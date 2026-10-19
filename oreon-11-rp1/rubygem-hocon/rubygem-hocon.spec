%global source1_hash ae74defe909ace97f8406393e4cd7a7c34454c3c99bbb712dbb4a67fbc31e5f6
%global source0_hash e71023ed7c56ae780ec34c0ce7789a233bcead08c045d50bc7b3af40f5afcd80
%global gem_name hocon
%if 0%{?el7}
%global enable_checks 0
%else
%global enable_checks 1
%endif
Name: rubygem-%{gem_name}
Version: 1.4.0
Release:        1%{?dist}
Summary:        HOCON Config Library
License: Apache-2.0
URL: https://github.com/puppetlabs/ruby-hocon
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/puppetlabs/ruby-hocon/archive/%{version}/ruby-hocon-%{version}.tar.gz
%if 0%{?enable_checks}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A port of the Java Typesafe Config
library to Ruby.
https://github.com/typesafehub/config

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
sed -i 's/\/usr\/bin\/env ruby/\/usr\/bin\/ruby/' bin/hocon

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} ruby-hocon-%{version}/spec --strip-components 1

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{gem_instdir}/bin/hocon %{buildroot}/%{_bindir}/hocon
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?enable_checks}
rspec spec/
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-hocon-doc -f %{oreon_filedir}/rubygem-hocon-doc.list

%changelog

%autochangelog
