%global source0_hash 7faaa912c5888d6e348d20fa31209b6409f1574346b1b80e309dbc7e8d63efac

%global gem_name rugged

Summary:       Rugged is a Ruby binding to the libgit2 library
Name:          rubygem-%{gem_name}
Version:       1.9.0
Release:       5%{?dist}

License:       MIT
URL:           https://github.com/libgit2/rugged
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/libgit2/rugged/pull/985
Patch:         985.patch

Requires:      ruby(rubygems)
Requires:      ruby
BuildRequires: gcc
BuildRequires: ruby
BuildRequires: cmake
BuildRequires: libgit2-devel >= %{version}
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygems-devel
Provides:      rubygem(%{gem_name}) = %{version}

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

# move C extensions to the extdir.
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}/} %{buildroot}%{gem_extdir_mri}/

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/ext/

%files
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
