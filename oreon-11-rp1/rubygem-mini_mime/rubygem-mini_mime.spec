%global source0_hash 30f2cca8a3c62b5c067f73a1834479dbd85d71f1291d65ffac933dc90796674d
%global gem_name mini_mime
Name: rubygem-%{gem_name}
Version: 1.1.0
Release:        11%{?dist}
Summary:        A lightweight mime type lookup toy
License: MIT
URL: https://github.com/discourse/mini_mime
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-test.txz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Minimal mime type implementation for use with the mail and rest-client gem.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

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
ln -s %{_builddir}/test .
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mini_mime-doc -f %{oreon_filedir}/rubygem-mini_mime-doc.list

%changelog

%autochangelog
