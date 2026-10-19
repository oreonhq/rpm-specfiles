%global source0_hash 238d774a58723d6c090494c8879b5e9918c19485f7e840f2c1c7532cf84ebcb1
%global gem_name jmespath
%global use_tests 1
Name:           rubygem-%{gem_name}
Version:        1.6.2
Release:        1%{?dist}
Summary:        JMESPath - Ruby Edition
License:        Apache-2.0
URL:            http://github.com/trevorrowe/jmespath.rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-repo.tgz
BuildArch:      noarch
%if 0%{?use_tests}
%endif
Requires:       rubygem(json)
# oreon:deps
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Implements JMESPath for Ruby.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version} -a 1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
cp -a CHANGELOG.md README.md %{buildroot}%{gem_instdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?use_tests}
cp -pr spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
echo "require 'jmespath'" > spec/spec_helper.rb
rm -f spec/compliance/identifiers.json
rspec -Ilib spec
rm -rf spec/
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-jmespath-doc -f %{oreon_filedir}/rubygem-jmespath-doc.list

%changelog

%autochangelog
