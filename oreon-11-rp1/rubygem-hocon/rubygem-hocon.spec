%global source0_hash e71023ed7c56ae780ec34c0ce7789a233bcead08c045d50bc7b3af40f5afcd80

# Generated from hocon-0.9.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hocon

%if 0%{?el7}
%global enable_checks 0
%else
%global enable_checks 1
%endif

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 9%{?dist}
Summary: HOCON Config Library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/puppetlabs/ruby-hocon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# SOURCE1 contains the upstream tag of the project from github
# in particular this includes the spec directory which was not
# included in the gemfile.
# https://github.com/puppetlabs/ruby-hocon/issues/65
# was originally resolved.
# However the rspec files were then removed again for a bizare reason.
# https://tickets.puppetlabs.com/browse/PA-2942
Source1: https://github.com/puppetlabs/ruby-hocon/archive/%{version}/ruby-hocon-%{version}.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.0
%if 0%{?enable_checks}
BuildRequires: rubygem(rspec)
%endif
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{gem_instdir}/bin/hocon %{buildroot}/%{_bindir}/hocon

%check
%if 0%{?enable_checks}
rspec spec/
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/spec
%{gem_spec}
%{_bindir}/hocon

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
