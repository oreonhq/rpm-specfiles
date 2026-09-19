%global source0_hash 73bf101929a1570e8034058e1296fec58d6c3386c26bf26810d33f70dd4236b7

%global gem_name narray

Name:           rubygem-%{gem_name}
Version:        0.6.1.2
Release:        4%{?dist}
Summary:        N-dimensional Numerical Array class for Ruby

# Automatically converted from old format: BSD and Ruby - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Ruby
URL:            http://%{gem_name}.rubyforge.org
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Patch0000:      https://github.com/masa16/narray/compare/0.6.1.2...master.patch#/%{name}-%{version}-last-commit.patch

BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
NArray is a Numerical N-dimensional Array class.  Supported element types are
1/2/4-byte Integer, single/double-precision, Real/Complex and Ruby Object.
This extension library incorporates fast calculation and easy manipulation of
large numerical arrays into the Ruby language.  NArray has features similar to
NumPy, but NArray has vector and matrix sub-classes.

%package devel
Summary:        Development files and developer's docs for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}

%description devel
This package contains the development files and the developer's documentation
for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{gem_name}-%{version}

%build
export CONFIGURE_ARGS="--with-cflags='-std=c99 %{build_cflags}'"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
# Copy to buildroot.
cp -a ./%{_prefix} %{buildroot}

# Clean-up.
pushd %{buildroot}
find .%{gem_instdir} -depth -type f -name '*.so' -print0 | xargs -0 rm -rf
find . -depth -type f -name '.*' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.log' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.o' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.out' -print0 | xargs -0 rm -rf
find . -depth -size 0 -type f -print0 | xargs -0 rm -rf
rm -rf .%{gem_cache} .%{gem_instdir}/src .%{gem_instdir}/%{gem_name}.gemspec
touch %{buildroot}%{gem_extdir_mri}/gem.build_complete
popd

%files
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/README.*
%dir %{gem_instdir}
%exclude %{gem_instdir}/MANIFEST
%exclude %{gem_instdir}/SPEC.*
%exclude %{gem_extdir_mri}/*.h
%{gem_extdir_mri}
%{gem_spec}

%files devel
%doc %{gem_docdir}
%doc %{gem_instdir}/MANIFEST
%doc %{gem_instdir}/SPEC.*
%{gem_extdir_mri}/*.h

%changelog
%autochangelog
