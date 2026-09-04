%global source0_hash 80ba0d373ba2f8fdb3148aa347e8c6ad11749b8cf4a4979e37946b3425f2c8bf

Name:          ckeditor
Version:       4.22.1
Release:       9%{?dist}
Summary:       WYSIWYG text editor to be used inside web pages

# Automatically converted from old format: GPLv2+ or LGPLv2+ or MPLv1.1 - review is highly recommended.
License:       GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+ OR LicenseRef-Callaway-MPLv1.1
URL:           http://ckeditor.com/

Source0:       http://download.cksource.com/CKEditor/CKEditor/CKEditor%20%{version}/ckeditor_%{version}_standard.tar.gz

BuildArch:     noarch
BuildRequires: web-assets-devel

Requires:      web-assets-filesystem

%description
CKEditor is a text editor to be used inside web pages. It's a WYSIWYG editor,
which means that the text being edited on it looks as similar as possible to
the results users have when publishing it. It brings to the web common editing
features found on desktop editing applications like Microsoft Word and
OpenOffice.

%package samples
Summary:  Samples for %{name}
Requires: %{name} = %{version}-%{release}

%description samples
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}

: Licenses
mkdir -p .rpm/{licenses,docs}
for LICENSE_FILE in $(find . -type f -name 'LICENSE*')
do
    DIR=$(dirname $LICENSE_FILE)
    mkdir -p .rpm/licenses/$DIR
    mv $LICENSE_FILE .rpm/licenses/$DIR/
done

: Docs
for DOC_FILE in $(find . -type f -name '*.md' -not -name 'LICENSE*')
do
    DIR=$(dirname $DOC_FILE)
    mkdir -p .rpm/docs/$DIR
    mv $DOC_FILE .rpm/docs/$DIR/
done

: wrong-file-end-of-line-encoding
find .rpm -type f -print0 | xargs -0 sed -i 's/\r$//'

: Delete bundled flash files
rm -rf samples/old/htmlwriter/{assets,outputforflash.html}

%build
# Empty build section, nothing to build

%install
mkdir -p %{buildroot}%{_webassetdir}/%{name}
cp -pr * %{buildroot}%{_webassetdir}/%{name}/

: Compat filesystem
mkdir -p %{buildroot}/%{_datadir}
ln -s %{_webassetdir}/%{name} %{buildroot}/%{_datadir}/%{name}

# https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Scriptlet_to_replace_a_directory
%pretrans -p <lua>
path = "%{_datadir}/%{name}"
st = posix.stat(path)
if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
        suffix = 0
        while not status do
            suffix = suffix + 1
            status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
        end
        os.rename(path, path .. ".rpmmoved")
    end
end

%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{_webassetdir}/%{name}
%{_datadir}/%{name}
%exclude %{_webassetdir}/%{name}/samples

%ghost %attr(644, root, root) %{_datadir}/%{name}.rpmmoved

%files samples
%{_webassetdir}/%{name}/samples

%changelog
%autochangelog
