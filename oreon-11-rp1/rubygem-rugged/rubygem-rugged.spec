%global source0_hash 7faaa912c5888d6e348d20fa31209b6409f1574346b1b80e309dbc7e8d63efac
%global gem_name rugged
Summary:        Rugged is a Ruby binding to the libgit2 library
Name:          rubygem-%{gem_name}
Version:       1.9.0
Release:        1%{?dist}
License:       MIT
URL:           https://github.com/libgit2/rugged
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch:         985.patch
Requires:      ruby(rubygems)
Requires:      ruby
Provides:      rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libgit2-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rugged is a Ruby bindings to the libgit2W C Git library. This is
for testing and using the libgit2 library in a language that is awesome.

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1

rm -vrf vendor
# Remove the bundled libraries from gemspec
sed -i -e 's\, "vendor[^,]*"\\g' ../%{gem_name}-%{version}.gemspec

# The build system requires libgit2's version.h to be present, and defaults to
# using the vendor'd copy. Use the system copy instead.
sed -i -e 's|LIBGIT2_DIR = .*|LIBGIT2_DIR = "%{_prefix}"|' ext/rugged/extconf.rb

%build

export CONFIGURE_ARGS="--with-cflags='%{optflags}' --use-system-libraries"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}/} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-rugged-doc -f %{oreon_filedir}/rubygem-rugged-doc.list

%changelog

%autochangelog
