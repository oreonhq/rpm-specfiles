%global source1_hash 9fc067f44c39d710685a20e22ef99c7fe736481126087b23c2cbae809295475c
%global source0_hash c29ada31c0f750b1d10c1a20442d015dc5052b80548b68d421bfded7adde2f87
%global gem_name dalli
%bcond_with tests
Name: rubygem-%{gem_name}
Version: 3.2.0
Release:        1%{?dist}
Summary:        High performance memcached client for Ruby
License: MIT
URL: https://github.com/petergoldstein/dalli
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/petergoldstein/dalli/archive/refs/tags/v3.2.0.tar.gz
%if %{with tests}
%endif
Requires:  rubygem(base64)
BuildArch: noarch
# oreon:deps
BuildRequires:  memcached
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(connection_pool)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
High performance memcached client for Ruby

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
pushd .%{gem_instdir}
ln -s %{_builddir}/test .
sed -i '/bundler/ s/^/#/' test/helper.rb
ruby -Ilib:test -rdalli -e "Dir.glob('./test/test_*.rb').sort.each{ |x| require x }"
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-dalli-doc -f %{oreon_filedir}/rubygem-dalli-doc.list

%changelog

%autochangelog
