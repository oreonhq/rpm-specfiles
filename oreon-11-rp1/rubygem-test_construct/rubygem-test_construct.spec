%global source0_hash 7e0752ca445bdbe378506a9f20ceb9e822ea1bb1f9ef990dfc241f2a12cf079f
%global gem_name test_construct
Name: rubygem-%{gem_name}
Version: 2.0.2
Release:        1%{?dist}
Summary:        Creates temporary files and directories for testing
License: MIT
URL: https://github.com/bhb/test_construct
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-test_construct-2.0.2-Fix-compatibility-with-Mocha-2.0.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Creates temporary files and directories for testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

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
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-test_construct-doc -f %{oreon_filedir}/rubygem-test_construct-doc.list

%changelog

%autochangelog
