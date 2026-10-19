%global source0_hash 533db7f7e5acafea1a145d6c5329cef667a58fbcb7d64379a808ff1199ee1b00
%global gem_name scanf
Name: rubygem-%{gem_name}
Version: 1.0.0
Release:        1%{?dist}
Summary:        A Ruby implementation of the C function scanf(3)
License: LicenseRef-Callaway-BSD
URL: https://github.com/ruby/scanf
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: LICENSE.txt
Source2: data.txt
Source3: test_scanf.rb
Source4: test_scanfblocks.rb
Source5: test_scanfio.rb
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A Ruby implementation of the C function scanf(3).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
cp %{SOURCE1} LICENSE.txt

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ruby -I.%{gem_instdir}/lib %{SOURCE3} %{SOURCE4} %{SOURCE5}
%files -f %{oreon_filedir}/main.list
%files -n rubygem-scanf-doc -f %{oreon_filedir}/rubygem-scanf-doc.list

%changelog

%autochangelog
