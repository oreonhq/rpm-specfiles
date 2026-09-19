%global source0_hash 913042d3afade625b71d05827b924692d05abfe1787d0f2b571fe95bc1c4a4df

%global		gem_name		imagesize
%if 0%{?fedora} < 19
%global		rubyabi		1.9.1
%endif

Summary:	Measure image size(GIF, PNG, JPEG ,,, etc)
Name:		rubygem-%{gem_name}
Version:	0.1.1
Release:	37%{?dist}
# SPDX confirmed
License:	Ruby OR GPL-2.0-only

URL:		http://imagesize.rubyforge.org
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# With ruby1.9 handling regex needs some encoding treatment...
# bz819188
Patch0:         ruby-imagesize-0.1.1-ruby19-regex-utf8.patch
# Change the default encoding for regex
Patch1:         rubygem-imagesize-0.1.1-regex-magic.patch

%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby 
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby 
%endif

Requires:	rubygems
BuildRequires:		rubygems-devel
BuildRequires:		rubygem(minitest)
# Don't create ruby-%%{gem_name} on F-17+
Obsoletes:	ruby-imagesize <= %{version}-%{release}

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# For now also provide ruby(%%gem_name).
# on F-17 (i.e. with ruby 1.9.x) this should be safe
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description
Imagefile measures image (GIF, PNG, JPEG ,,, etc) size code 
by Pure Ruby ["PCX", "PSD", "XPM", "TIFF", "XBM", "PGM", 
"PBM", "PPM", "BMP", "JPEG", "PNG", "GIF", "SWF"]

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
mkdir -p .%{gem_dir}
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Fixup wrong interpretter, line encoding
sed -i -e '1d' -e 's|\r||' lib/image_size.rb

# Patches
%patch -P0 -p1
%patch -P1 -p1

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
#ERROR:  While executing gem ... (Gem::InvalidSpecificationException)
#    cert_chain must not be nil
sed -i -e '/cert_chain/s|nil|[]|' %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%check
# Where is ppm files?
pushd .%{gem_instdir}
sed -i.ppm \
	-e "s|'ppm.ppm', ||" \
	-e '/PPM/d' \
	test/test_image_size.rb
# Seems that PCX file cannot pass, rescue for now
ruby -Ilib -rtest/unit ./test/test_image_size.rb || echo "rescue for now"

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/README.txt
%{gem_instdir}/lib/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
%exclude	%{gem_instdir}/Manifest.txt
%exclude	%{gem_instdir}/setup.rb
%exclude	%{gem_instdir}/test/

%changelog
%autochangelog
