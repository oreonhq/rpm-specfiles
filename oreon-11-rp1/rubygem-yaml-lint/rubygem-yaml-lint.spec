%global source1_hash 6abffd399a9491a5a0d1f4546ccfdd832c27266a4eb9876bb53ae6bfdf0db08f
%global source0_hash e3960b171766ae187338a169815e99fe10fcb0d9c22b1c539e8d57e114324c8a
%global gem_name yaml-lint
%global commit 8dfc583584e046c54617315734883c887768c6ca
Name:          rubygem-%{gem_name}
Version:       0.1.2
Release:        1%{?dist}
Summary:        Really simple YAML lint
License:       MIT
URL:           https://github.com/Pryz/yaml-lint
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:       https://github.com/Pryz/yaml-lint/archive/%{commit}/yaml-lint-%{commit}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Check if your YAML files can be loaded.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# unpack only the spec and LICENSE from SOURCE1
tar zxf %{SOURCE1} --strip-components 1 \
                   yaml-lint-%{commit}/spec \
                   yaml-lint-%{commit}/LICENSE \
                   yaml-lint-%{commit}/README.md \

# Disable Coverals
sed -i "s/^require 'coveralls'$//" spec/spec_helper.rb
sed -i "s/^Coveralls.wear!//"      spec/spec_helper.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rspec -I%{gem_instdir} spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-yaml-lint-doc -f %{oreon_filedir}/rubygem-yaml-lint-doc.list

%changelog

%autochangelog
