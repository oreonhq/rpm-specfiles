%global source0_hash 2f8bd142ef69a1a29637bc56804163ef9a0a398fd349bf9d4a3c67c4dfa82557
%global	gem_name test-unit-ruby-core
Name:		rubygem-%{gem_name}
Version:	1.0.16
Release:        1%{?dist}
Summary:        Additional test assertions for Ruby standard libraries
License:	BSD-2-Clause OR Ruby
URL:		https://github.com/ruby/test-unit-ruby-core
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-additional.tar.gz
Source2:	test-unit-ruby-core-create-missing-files.sh
BuildArch:		noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Additional test assertions for Ruby standard libraries.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
cp -a \
	BSDL \
	COPYING \
	README.md \
	%{buildroot}%{gem_instdir}/
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

exit 0
%files -f %{oreon_filedir}/main.list
%files -n rubygem-test-unit-ruby-core-doc -f %{oreon_filedir}/rubygem-test-unit-ruby-core-doc.list

%changelog

%autochangelog
