%global source1_hash c33019c1e16d234abe063ba1d99901aab95c9b606edf4c682c57f16a1186e47d
%global source0_hash d5ea2ed61a720a220f1914778208e718a0c7ed2a484b6d357ba695aa7001390f
%global gem_name rchardet
Name: rubygem-%{gem_name}
Version: 1.10.0
Release:        1%{?dist}
Summary:        Character encoding auto-detection in Ruby
License: LicenseRef-Callaway-LGPLv2
URL: https://github.com/jmhodges/rchardet
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/jmhodges/rchardet/archive/v%{version}/rchardet-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Character encoding auto-detection in Ruby. As smart as your browser.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

tar zxf %{SOURCE1} rchardet-%{version}/test rchardet-%{version}/LGPL-LICENSE.txt rchardet-%{version}/Readme.md --strip-components 1
# Remove +x bit on license.
chmod 0644 LGPL-LICENSE.txt

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rchardet-doc -f %{oreon_filedir}/rubygem-rchardet-doc.list

%changelog

%autochangelog
