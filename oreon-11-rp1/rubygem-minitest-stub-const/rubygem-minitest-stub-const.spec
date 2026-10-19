%global source0_hash b39f34dd6b8e7045fcc36820083aceaa68075318e4c4f365b12f11bd5f34b279
%global gem_name minitest-stub-const
Name: rubygem-%{gem_name}
Version: 0.6
Release:        1%{?dist}
Summary:        Stub constants for the duration of a block in MiniTest
License: MIT
URL: https://github.com/adammck/minitest-stub-const
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-minitest-stub-const-0.6-Fix-compatibility-with-Minitest-5.19.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Stub constants for the duration of a block in MiniTest.

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
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-minitest-stub-const-doc -f %{oreon_filedir}/rubygem-minitest-stub-const-doc.list

%changelog

%autochangelog
