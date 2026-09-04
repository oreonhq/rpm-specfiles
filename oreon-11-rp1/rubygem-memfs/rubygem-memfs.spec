%global source0_hash 182e18c7b414e44670b0d8329f82f9787d58649a5c3bd6ec2b433a9918b2f3a1

%global gem_name memfs

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 26%{?dist}
Summary: Fake file system that can be used for tests
License: MIT
URL: http://github.com/simonc/memfs
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/simonc/memfs/commit/d8e61aba482fe3167e6399a888763ce2a796b30d
Patch0: 0001_file_extname_27_behavior.patch
# https://github.com/simonc/memfs/pull/40
# Fix handling of kwargs with rspec-mocks 3.12+
Patch1: 0002-kwargs-handling-fix.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) => 3.0
BuildRequires: rubygem(rspec) < 4
BuildArch: noarch

%description
MemFs provides a fake file system that can be used for tests. Strongly
inspired by FakeFS.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# We don't care about coverage.
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
# This is temporary due to https://github.com/simonc/memfs/issues/27
# Include the file if version > 1.0.0
rm spec/fileutils_spec.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/memfs.png
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/memfs.png
%{gem_instdir}/Rakefile
%{gem_instdir}/memfs.gemspec
%{gem_instdir}/spec
%{gem_instdir}/Guardfile

%changelog
%autochangelog
