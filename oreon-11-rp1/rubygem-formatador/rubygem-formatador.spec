%global source0_hash 19fa898133c2c26cdbb5d09f6998c1e137ad9427a046663e55adfe18b950d894
%global gem_name formatador
%{!?_with_bootstrap: %global bootstrap 0}
Name: rubygem-%{gem_name}
Version: 1.2.3
Release:        2%{?dist}
Summary:        Ruby STDOUT text formatting
License: MIT
URL: https://github.com/geemus/formatador
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if ! 0%{?bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(reline)
BuildRequires:  rubygem(shindo)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
STDOUT text formatting.

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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if ! 0%{?bootstrap}
pushd .%{gem_instdir}
RUBYOPT=-Ilib shindo
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-formatador-doc -f %{oreon_filedir}/rubygem-formatador-doc.list

%changelog

%autochangelog
