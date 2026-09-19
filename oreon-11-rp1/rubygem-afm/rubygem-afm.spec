%global source0_hash c83e698e759ab0063331ff84ca39c4673b03318f4ddcbe8e90177dd01e4c721a

# Generated from afm-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name afm

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 24%{?dist}
Summary: Reading Adobe Font Metrics (afm) files
License: MIT
URL: http://github.com/halfbyte/afm
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple library to read afm files and use the data conveniently.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Get rid of Bundler
sed -i -e '2d' ./test/helper.rb
ruby -Ilib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/LICENSE
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
