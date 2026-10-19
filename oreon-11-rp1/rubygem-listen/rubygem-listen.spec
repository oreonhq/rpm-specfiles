%global source1_hash 729bd7ae03e3e617ddd4408d0b4f3681970d28c6271ba56a629229250cdb0997
%global source0_hash 3b80caa7aa77fae836916c2f9e3fbcafbd15f5d695dd487c1f5b5e7e465efe29
%global gem_name listen
Name: rubygem-%{gem_name}
Version: 3.7.1
Release:        10%{?dist}
Summary:        Listen to file modifications
License: MIT
URL: https://github.com/guard/listen
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/guard/listen/archive/refs/tags/v3.7.1.tar.gz
Patch0: rubygem-listen-3.7.1-Fix-kwargs-matching-with-rspec-mock-3.12-and-Ruby-3.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(rb-inotify)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(thor)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
ln -s %{_builddir}/spec spec
mv spec/lib/listen/adapter/darwin_spec.rb{,.disabled}
rspec -rspec_helper spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-listen-doc -f %{oreon_filedir}/rubygem-listen-doc.list

%changelog

%autochangelog
