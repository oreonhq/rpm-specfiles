%global source0_hash 3b80caa7aa77fae836916c2f9e3fbcafbd15f5d695dd487c1f5b5e7e465efe29

# Generated from listen-0.4.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name listen

Name: rubygem-%{gem_name}
Version: 3.7.1
Release: 10%{?dist}
Summary: Listen to file modifications
License: MIT
URL: https://github.com/guard/listen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/guard/listen.git --no-checkout
# cd listen && git archive -v -o rubygem-listen-3.7.1-spec.txz v3.7.1 spec
Source1: rubygem-listen-%{version}-spec.txz
# Fix kwargs matching compatibility with RSpec 3.12+.
# https://github.com/guard/listen/pull/564
Patch0: rubygem-listen-3.7.1-Fix-kwargs-matching-with-rspec-mock-3.12-and-Ruby-3.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(logger)
BuildRequires: rubygem(rb-inotify)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
The Listen gem listens to file modifications and notifies you about the
changes. Works everywhere!

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch 0 -p1
popd

# Remove the hardcoded dependencies. We don't have them in Fedora
# (except rb-inotify), they are platform specific and not needed.
# https://github.com/guard/listen/pull/54
%gemspec_remove_dep -g rb-fsevent [">= 0.10.3", "~> 0.10"]
# https://github.com/guard/listen/pull/587
%gemspec_add_dep -g logger
sed -i '/def self.usable?$/a         return false' lib/listen/adapter/darwin.rb

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
# Move the tests into place
ln -s %{_builddir}/spec spec

# We removed dependencies from other platforms so let's remove
# tests as well
mv spec/lib/listen/adapter/darwin_spec.rb{,.disabled}

rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/listen
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
