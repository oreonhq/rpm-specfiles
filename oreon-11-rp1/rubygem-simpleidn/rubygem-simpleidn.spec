%global source0_hash 35dda985b761dff5751fefa7fba02e477427c975d47b11c4c4ffaf01afe1c719

%global gem_name simpleidn

Name: rubygem-%{gem_name}
Version: 0.2.1
Release: 11%{?dist}
Summary: Punycode ACE to unicode UTF-8 (and vice-versa) string conversion
License: MIT
URL: https://github.com/mmriis/simpleidn
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2
# BuildRequires: rubygem(rspec) >= 3.0
# BuildRequires: rubygem(rspec) < 4
BuildArch: noarch

%description
This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
# relax unf dependency
sed -i ../%{gem_name}-%{version}.gemspec -e '\@unf@s|0.1.4|0.1|'

# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
chmod 755 %{buildroot}%{gem_instdir}/tables/generate_mapping_table.rb

%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENCE
%{gem_libdir}
%{gem_instdir}/tables
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/simpleidn.gemspec

%changelog
%autochangelog
