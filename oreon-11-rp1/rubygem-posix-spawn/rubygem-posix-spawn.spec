%global source0_hash a2e0109bf9b9e041e74359aba9d6e9e92c1122cbdb15f6e9779d61aab606ab32
%global gem_name posix-spawn
Name: rubygem-%{gem_name}
Version: 0.3.15
Release:        19%{?dist}
Summary:        posix_spawnp(2) for Ruby
License: MIT
URL: https://github.com/rtomayko/posix-spawn
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-posix-spawn-0.3.11-skip-tests.patch
Patch1: posix-spawn-0.3.15-c99-comformant.patch
%if 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems)
%endif
%if 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
posix-spawn uses posix_spawnp(2) for faster process spawning.

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

# Remove developer-only files.
FREEZE=""
for f in .gitignore Gemfile Rakefile; do
  rm $f
  sed -i "s|\"$f\"${FREEZE},||g" %{gem_name}.gemspec
done

# Skip tests that fail.
# https://github.com/rtomayko/posix-spawn/issues/43
%patch -P0 -p1
%patch -P1 -p1

%build

gem build %{gem_name}.gemspec
%gem_install
rm .%{gem_instdir}/%{gem_name}.gemspec
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -r %{buildroot}%{gem_instdir}/ext
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -pa .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
  ruby -I"lib:test:%{buildroot}%{gem_extdir_mri}" -e \
    'Dir.glob "./test/test_*.rb", &method(:require)' || :
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-posix-spawn-doc -f %{oreon_filedir}/rubygem-posix-spawn-doc.list

%changelog

%autochangelog
