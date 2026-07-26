%global source0_hash 2149ed7efc3097ae65eb5a2a1e22ee86efbdaef56fb81136211b3d10618fd862

# Generated from shindo-0.3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name shindo

Name: rubygem-%{gem_name}
Version: 0.3.10
Release: 12%{?dist}
Summary: Simple depth first Ruby testing
License: MIT
URL: http://github.com/geemus/shindo
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/geemus/shindo/pull/29
# ruby3.2 removes File.exists? already deprecated since ruby2.1
Patch0:  %{name}-0.3.10-ruby32-File-exists-removal.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(formatador) >= 0.1.1
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
bin/shindo
popd

%files
%dir %{gem_instdir}
%{_bindir}/shindo
%{_bindir}/shindont
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/shindo.gemspec
%{gem_instdir}/tests

%changelog
%autochangelog
