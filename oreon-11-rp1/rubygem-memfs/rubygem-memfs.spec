%global source0_hash 182e18c7b414e44670b0d8329f82f9787d58649a5c3bd6ec2b433a9918b2f3a1
%global gem_name memfs
Name: rubygem-%{gem_name}
Version: 1.0.0
Release:        26%{?dist}
Summary:        Fake file system that can be used for tests
License: MIT
URL: http://github.com/simonc/memfs
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: 0001_file_extname_27_behavior.patch
Patch1: 0002-kwargs-handling-fix.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
rm spec/fileutils_spec.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-memfs-doc -f %{oreon_filedir}/rubygem-memfs-doc.list

%changelog

%autochangelog
