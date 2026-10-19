%global source0_hash 35dda985b761dff5751fefa7fba02e477427c975d47b11c4c4ffaf01afe1c719
%global gem_name simpleidn
Name: rubygem-%{gem_name}
Version: 0.2.1
Release:        11%{?dist}
Summary:        Punycode ACE to unicode UTF-8 (and vice-versa) string conversion
License: MIT
URL: https://github.com/mmriis/simpleidn
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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

sed -i ../%{gem_name}-%{version}.gemspec -e '\@unf@s|0.1.4|0.1|'
gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
chmod 755 %{buildroot}%{gem_instdir}/tables/generate_mapping_table.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-simpleidn-doc -f %{oreon_filedir}/rubygem-simpleidn-doc.list

%changelog

%autochangelog
