%global source0_hash 579ac5fc5cafdac7db6898ba104ca537a03ab079253334aea2de9c347c4e47f5
%global gem_name xmlrpc
Name: rubygem-%{gem_name}
Version: 0.3.2
Release:        1%{?dist}
Summary:        XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP
License: Ruby OR LicenseRef-Callaway-BSD
URL: https://github.com/ruby/xmlrpc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: xmlrpc-%{version}-tests.txz
Patch0:  xmlrpc-pr54-remover-logger-dep.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
XMLRPC is a lightweight protocol that enables remote procedure calls over
HTTP.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
(
cd %{_builddir}
%patch -P0 -p1
)

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
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-xmlrpc-doc -f %{oreon_filedir}/rubygem-xmlrpc-doc.list

%changelog

%autochangelog
