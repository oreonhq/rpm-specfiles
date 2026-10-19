%global source0_hash 2149ed7efc3097ae65eb5a2a1e22ee86efbdaef56fb81136211b3d10618fd862
%global gem_name shindo
Name: rubygem-%{gem_name}
Version: 0.3.10
Release:        12%{?dist}
Summary:        Simple depth first Ruby testing
License: MIT
URL: http://github.com/geemus/shindo
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  %{name}-0.3.10-ruby32-File-exists-removal.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(formatador)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Work with your tests, not against them.

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
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
bin/shindo
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-shindo-doc -f %{oreon_filedir}/rubygem-shindo-doc.list

%changelog

%autochangelog
