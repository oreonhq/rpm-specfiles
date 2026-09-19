%global source0_hash 30b5237f0603f6662ab8d1fc2bd4a96142b806c6415d79e45ef5fdc6a0cfc837

%global gem_name colorize

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 5%{?dist}
Summary: Add color methods to String class
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/fazibear/colorize
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: rubygem-minitest
BuildArch: noarch

%description
Ruby String class extension. Adds methods to set text color, background color 
and, text effects on ruby console and command line output, using ANSI escape 
sequences.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}

rm -f .%{gem_instdir}/Rakefile
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
