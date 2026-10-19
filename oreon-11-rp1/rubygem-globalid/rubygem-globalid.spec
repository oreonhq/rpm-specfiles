%global source1_hash 0cb9f9830ad24bd7675f3196ce47c58c55502cb8c4cd2d146f95f3e78769f23a
%global source0_hash 70bf76711871f843dbba72beb8613229a49429d1866828476f9c9d6ccc327ce9
%global gem_name globalid
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 1.2.1
Release:        1%{?dist}
Summary:        Refer to any model with a URI: gid://app/class/id
License: MIT
URL: http://www.rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/globalid/archive/refs/tags/v1.2.1.tar.gz
Patch0: rubygem-globalid-1.2.1-Keep-using-URI-RFC2396-parser.patch
Patch1: rubygem-globalid-1.2.1-Fix-cache-format-for-Rails-8.patch
%if %{without bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
URIs for your models makes it easy to pass references around.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1

( cd %{builddir}
%patch 1 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
sed -i "/bundler\/setup/ s/^/#/" ./test/helper.rb
ruby -Ilib:test -raction_controller -e "Dir.glob './test/cases/*test.rb', &method(:require)"
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-globalid-doc -f %{oreon_filedir}/rubygem-globalid-doc.list

%changelog

%autochangelog
