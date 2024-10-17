Summary:	Create a shadow directory of symbolic links to another directory tree
Name:		lndir
Version:	1.0.5
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto)

%description
The lndir program makes a shadow copy of a directory tree, except that
the shadow is not populated with real files but instead with symbolic links
pointing at the real files in the source directory tree. This is usually
useful for maintaining source code for different machine architectures. You
create a shadow directory containing links to the real source, which you will
have usually mounted from a remote machine. You can build in the shadow tree,
and the object files will be in the shadow directory, while the source files
in the shadow directory are just symlinks to the real files.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/lndir
%doc %{_mandir}/man1/lndir.*

